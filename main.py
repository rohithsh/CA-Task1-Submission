


#To write a pandas dataframe into a json file
def write_to_json_file(df, filename):
    df.to_json(filename, orient = 'records', indent=3)
    pass

def read_file(path, encoding_scheme):
    df = pd.read_csv(path, sep='\t', encoding=encoding_scheme)
    return df

def drop_non_arg_records():

    return

#Data transformation to split the characters from the effectiveness_score & argument_quality_score columns and merge the dataframes based on id
def data_transformation(df):
    df['argument_quality_score'] = (df['overall quality'].str.split(" ", expand=True)[0]).astype(float)
    df['effectiveness_score'] = (df['effectiveness'].str.split(" ", expand=True)[0]).astype(float)
    df2 = df[["#id", "issue", "stance", "argument"]].drop_duplicates()
    df3 = df.groupby("#id").agg(list).reset_index()[["#id", "argumentative", "argument_quality_score", "effectiveness_score"]]
    df_extract = df2.merge(df3, on='#id')
    return df_extract

def find_mean():

    return

def plot_correlation(df):
    df["effectiveness_score_mean"] = df["argument_quality_score"].apply(np.mean)
    df["argument_quality_score_mean"] = df["effectiveness_score"].apply(np.mean)
    cor_df = df.corr()
    sns.lmplot(x='effectiveness_score_mean',y='argument_quality_score_mean',data=df, fit_reg=True)
    return cor_df

def plot_histogram(df):
    df_count = df[["issue", "argumentative"]].groupby("issue")[["issue", "argumentative"]].apply(lambda x: x)
    df_count_pivot = df.pivot_table(index='issue', columns='argumentative', aggfunc='size', fill_value=0)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()
    width = 0.4
    x_labs = df[["issue"]].drop_duplicates().values
    df_pivot.plot(kind='bar', x='n', color='red', ax=ax, width=width, position=1)
    df_pivot.plot(kind='bar', x='y', color='blue', ax=ax, width=width, position=0)
    plt.xticks(np.arange(16), x_labs)
    ax.set_xlabel("issue")
    ax.set_ylabel('count')
    plt.show()
    pass

def main():
    path = "data/dagstuhl-15512-argquality-corpus-annotated.csv"
    encoding_scheme = "latin-1"
    df = read_file(path,encoding_scheme)
    #Choosing the necessary columns from the provided csv file
    df = df[["#id", "annotator", "issue", "stance", "argumentative", "overall quality", "effectiveness", "argument"]]
    df_extract = data_transformation(df)
    #Computing and plotting the graphs for the two statistics mentioned in the 'Readme' file
    plot_correlation(df_extract)
    plot_histogram(df_extract)

    pass


if __name__ == '__main__':
    main()
