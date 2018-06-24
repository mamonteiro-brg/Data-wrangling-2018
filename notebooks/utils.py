def clean_api_df(df,drop_columns=None):
	df = df.copy()
	if drop_columns is None:
		return df
	else:
		return df.drop(columns=drop_columns)