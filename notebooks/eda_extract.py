import os
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def main():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(base, 'DATASET')
    fig_dir = os.path.join(os.path.dirname(__file__), 'figures')
    os.makedirs(fig_dir, exist_ok=True)

    survey_path = os.path.join(data_dir, 'GenZ_Financial_Literacy_Survey.csv')
    profile_path = os.path.join(data_dir, 'GenZ_Financial_Profile.csv')
    regional_path = os.path.join(data_dir, 'Regional_Economic_Indicators.csv')

    def read_csv_any(path):
        for enc in ['utf-8', 'utf-8-sig', 'latin-1']:
            try:
                return pd.read_csv(path, encoding=enc, sep=';')
            except UnicodeDecodeError:
                continue
        # final fallback without encoding
        return pd.read_csv(path, engine='python', sep=';')

    survey = read_csv_any(survey_path)
    profile = read_csv_any(profile_path)
    regional = read_csv_any(regional_path)

    def df_overview(df, name):
        miss = df.isna().sum()
        miss_pct = (miss / len(df) * 100).round(2)
        dtypes = df.dtypes.astype(str)
        return {
            'name': name,
            'shape': [int(df.shape[0]), int(df.shape[1])],
            'columns': list(df.columns),
            'dtypes': dtypes.to_dict(),
            'missing_counts': miss.to_dict(),
            'missing_pct': miss_pct.to_dict(),
        }

    survey_info = df_overview(survey, 'GenZ_Financial_Literacy_Survey')
    profile_info = df_overview(profile, 'GenZ_Financial_Profile')
    regional_info = df_overview(regional, 'Regional_Economic_Indicators')

    # Clean monetary columns
    for col in ['Est. Monthly Income', 'Est. Monthly Expenditure']:
        if col in profile.columns:
            profile[col] = (
                profile[col]
                .astype(str)
                .str.replace(r"[^0-9.-]", "", regex=True)
                .replace({'': np.nan, '-': np.nan})
            )
            profile[col] = pd.to_numeric(profile[col], errors='coerce')

    # Also create explicit numeric copies to avoid dtype issues downstream
    if 'Est. Monthly Income' in profile.columns:
        profile['income_num'] = pd.to_numeric(
            profile['Est. Monthly Income']
                .astype(str)
                .str.replace(r"[^0-9.-]", "", regex=True)
                .replace({'': np.nan, '-': np.nan}), errors='coerce'
        )
    if 'Est. Monthly Expenditure' in profile.columns:
        profile['expense_num'] = pd.to_numeric(
            profile['Est. Monthly Expenditure']
                .astype(str)
                .str.replace(r"[^0-9.-]", "", regex=True)
                .replace({'': np.nan, '-': np.nan}), errors='coerce'
        )

    # Build financial anxiety score from relevant items (higher = more anxious)
    anxiety_items = [
        'Because of my money situation, I feel I will never have the things I want in life',
        'I am behind with my finances',
        'My finances control my life',
        'Whenever I feel in control of my finances, something happens that sets me back',
        'I am unable to enjoy life because I obsess too much about money'
    ]
    available_anx = [c for c in anxiety_items if c in profile.columns]
    if available_anx:
        profile['financial_anxiety_score'] = profile[available_anx].apply(pd.to_numeric, errors='coerce').mean(axis=1)

    # Numeric and categorical summaries for profile
    num_cols_profile = [c for c in profile.select_dtypes(include=[np.number]).columns]
    profile_desc = (
        profile[num_cols_profile].describe(percentiles=[.05, .25, .5, .75, .95]).to_dict()
        if num_cols_profile else {}
    )

    # Frequency tables for selected categoricals if present
    cat_distributions = {}
    for c in ['gender', 'province', 'education_level', 'employment_status', 'main_fintech_app', 'investment_type']:
        if c in profile.columns:
            vc = profile[c].value_counts(dropna=False)
            cat_distributions[c] = {
                'top': vc.head(10).to_dict(),
                'pct': (vc / len(profile) * 100).round(2).head(10).to_dict(),
            }

    # Derived metrics
    # Derived metrics using numeric copies if available
    if {'income_num', 'expense_num'}.issubset(profile.columns):
        income = profile['income_num']
        expense = profile['expense_num']
        with np.errstate(divide='ignore', invalid='ignore'):
            saving_rate = (income - expense) / income
        profile['saving_rate'] = saving_rate.replace([np.inf, -np.inf], np.nan)
    else:
        profile['saving_rate'] = np.nan

    # Correlations for selected vars
    candidate_corr_cols = [
        'financial_anxiety_score', 'income_num', 'expense_num',
        'saving_rate',
    ]
    available_corr_cols = [c for c in candidate_corr_cols if c in profile.columns]
    corr_matrix = (
        profile[available_corr_cols].corr(method='pearson') if available_corr_cols else pd.DataFrame()
    )

    # Plots
    if 'income_num' in profile.columns and profile['income_num'].notna().sum() > 0:
        plt.figure(figsize=(8, 5))
        sns.histplot(profile['income_num'].dropna(), bins=40, kde=True)
        plt.title('Distribusi Pendapatan Bulanan (IDR)')
        plt.xlabel('Pendapatan (IDR)')
        plt.ylabel('Frekuensi')
        plt.tight_layout()
        plt.savefig(os.path.join(fig_dir, 'distribution_income.png'), dpi=200)
        plt.close()

    if {'financial_anxiety_score', 'income_num'}.issubset(profile.columns):
        if profile[['financial_anxiety_score', 'income_num']].dropna().shape[0] > 0:
            plt.figure(figsize=(6, 5))
            sns.scatterplot(
                data=profile, x='income_num', y='financial_anxiety_score', alpha=0.4
            )
            try:
                sns.regplot(
                    data=profile, x='income_num', y='financial_anxiety_score', scatter=False, color='red'
                )
            except Exception:
                pass
            plt.title('Anxiety vs Pendapatan')
            plt.tight_layout()
            plt.savefig(os.path.join(fig_dir, 'fa_vs_income_scatter.png'), dpi=200)
            plt.close()

    if not corr_matrix.empty and corr_matrix.shape[0] > 1:
        plt.figure(figsize=(7, 6))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='BrBG', center=0)
        plt.title('Korelasi Variabel Utama (Profile)')
        plt.tight_layout()
        plt.savefig(os.path.join(fig_dir, 'correlation_heatmap.png'), dpi=200)
        plt.close()

    # Outlier report
    outlier_report = {}
    for col in ['income_num', 'expense_num']:
        if col in profile.columns:
            s = profile[col].dropna()
            if len(s) > 0:
                q1, q3 = np.percentile(s, [25, 75])
                iqr = q3 - q1
                lower = q1 - 1.5 * iqr
                upper = q3 + 1.5 * iqr
                outliers = ((profile[col] < lower) | (profile[col] > upper)).sum()
                outlier_report[col] = {
                    'q1': float(q1), 'q3': float(q3), 'iqr': float(iqr),
                    'lower': float(lower), 'upper': float(upper), 'outliers': int(outliers),
                }

    # Hypothesis tests
    results_tests = []

    # H1: Anxiety differs by gender (Mann-Whitney U)
    if {'financial_anxiety_score', 'Gender'}.issubset(profile.columns):
        g = profile[['financial_anxiety_score', 'Gender']].dropna()
        vals = g['Gender'].dropna().unique()
        if len(vals) == 2:
            a = g[g['Gender'] == vals[0]]['financial_anxiety_score'].values
            b = g[g['Gender'] == vals[1]]['financial_anxiety_score'].values
            if len(a) > 20 and len(b) > 20:
                stat, p = stats.mannwhitneyu(a, b, alternative='two-sided')
                results_tests.append({
                    'hypothesis': 'H1: Anxiety berbeda menurut gender',
                    'groups': [str(vals[0]), str(vals[1])],
                    'test': 'Mann-Whitney U', 'p_value': float(p), 'significant': bool(p < 0.05)
                })

    # H2: Anxiety differs by employment_status (Kruskal-Wallis)
    if {'financial_anxiety_score', 'Job'}.issubset(profile.columns):
        g = profile[['financial_anxiety_score', 'Job']].dropna()
        cats = g['Job'].value_counts()
        top_cats = cats[cats >= 20].index.tolist()
        if len(top_cats) >= 3:
            arrays = [g[g['Job'] == c]['financial_anxiety_score'].values for c in top_cats]
            stat, p = stats.kruskal(*arrays)
            results_tests.append({
                'hypothesis': 'H2: Anxiety berbeda antar status pekerjaan',
                'groups': top_cats,
                'test': 'Kruskal-Wallis', 'p_value': float(p), 'significant': bool(p < 0.05)
            })

    # H3: Saving rate differs by digital time (top vs bottom quartile) - MW U
    # Without digital time column in this dataset, we approximate H3 using impulsivity as proxy (top vs bottom quartile)
    if {'saving_rate', 'I am impulsive '}.issubset(profile.columns):
        df2 = profile[['saving_rate', 'I am impulsive ']].dropna()
        if len(df2) > 40:
            q1 = df2['I am impulsive '].quantile(0.25)
            q3 = df2['I am impulsive '].quantile(0.75)
            low = df2[df2['I am impulsive '] <= q1]['saving_rate'].dropna()
            high = df2[df2['I am impulsive '] >= q3]['saving_rate'].dropna()
            if len(low) > 20 and len(high) > 20:
                stat, p = stats.mannwhitneyu(low, high, alternative='two-sided')
                results_tests.append({
                    'hypothesis': 'H3: Saving rate berbeda antara impulsivitas rendah vs tinggi',
                    'test': 'Mann-Whitney U', 'p_value': float(p), 'significant': bool(p < 0.05)
                })

    # H4: Anxiety vs saving_rate correlation (Spearman)
    if {'financial_anxiety_score', 'saving_rate'}.issubset(profile.columns):
        s1 = profile['financial_anxiety_score']
        s2 = profile['saving_rate']
        m = s1.notna() & s2.notna()
        if m.sum() > 30:
            rho, p = stats.spearmanr(s1[m], s2[m])
            results_tests.append({
                'hypothesis': 'H4: Anxiety berkorelasi dengan saving rate',
                'test': 'Spearman', 'rho': float(rho), 'p_value': float(p), 'significant': bool(p < 0.05)
            })

    # H5: Spearman correlation Anxiety vs Outstanding Loan
    # H5: Anxiety vs age (proxied from Year of Birth) - younger cohort difference
    if {'financial_anxiety_score', 'Year of Birth'}.issubset(profile.columns):
        # Convert year to age approx as of 2025
        age = 2025 - profile['Year of Birth']
        s1 = profile['financial_anxiety_score']
        s2 = age
        mask = s1.notna() & s2.notna()
        if mask.sum() > 30:
            rho, p = stats.spearmanr(s1[mask], s2[mask])
            results_tests.append({
                'hypothesis': 'H5: Anxiety berkorelasi dengan usia',
                'test': 'Spearman', 'rho': float(rho), 'p_value': float(p), 'significant': bool(p < 0.05)
            })

    # Categorical distributions for actual column names
    cat_distributions = {}
    for c in ['Gender', 'Province of Origin', 'Last Education', 'Job', 'Residence Status']:
        if c in profile.columns:
            vc = profile[c].value_counts(dropna=False)
            cat_distributions[c] = {
                'top': vc.head(10).to_dict(),
                'pct': (vc / len(profile) * 100).round(2).head(10).to_dict(),
            }

    report = {
        'survey_info': survey_info,
        'profile_info': profile_info,
        'regional_info': regional_info,
        'profile_numeric_desc': profile_desc,
        'profile_cat_distributions': cat_distributions,
        'available_corr_cols': available_corr_cols,
        'corr_matrix': corr_matrix.round(3).to_dict() if not corr_matrix.empty else {},
        'outliers': outlier_report,
        'hypothesis_results': results_tests,
        'figures': [p for p in [
            os.path.join('notebooks', 'figures', 'distribution_income.png') if 'income_num' in profile.columns else None,
            os.path.join('notebooks', 'figures', 'fa_vs_income_scatter.png') if {'financial_anxiety_score','income_num'}.issubset(profile.columns) else None,
            os.path.join('notebooks', 'figures', 'correlation_heatmap.png') if not corr_matrix.empty and corr_matrix.shape[0] > 1 else None,
        ] if p],
    }

    out_path = os.path.join(os.path.dirname(__file__), 'eda_report.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps({
        'message': 'EDA report generated',
        'report_path': os.path.relpath(out_path, base),
        'figures': report['figures']
    }, ensure_ascii=False))

if __name__ == '__main__':
    main()
