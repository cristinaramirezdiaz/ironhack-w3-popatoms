import pandas as pd


def get_years_rank(chart_name = "hot-100-songs", start_year, end_year):
    
    """
    Retrieve Billboard chart data for a given range of years.

    Parameters
    ----------
    chart_name : str, optional
        The name of the Billboard chart to retrieve. Defaults to "hot-100-songs".
    start_year : int
        The first year of the range of years to retrieve.
    end_year : int
        The last year of the range of years to retrieve.

    Returns
    -------
    df : pandas.DataFrame
        A DataFrame containing the chart data for the given range of years. The columns are 'rank_year', 'title', 'artist', and 'rank'.
    """
    year_values = []
    artist_values = []
    title_values = []
    rank_values = []

    for year in range (start_year, end_year+1):
        chart = billboard.ChartData(chart_name, year=year)
        for entry in chart:
            year_values.append(year)
            title_values.append(entry.title)
            artist_values.append(entry.artist)
            rank_values.append(entry.rank)

    df = pd.DataFrame({'rank_year': year_values, 'title': title_values, 'artist': artist_values, 'rank': rank_values})
    return df