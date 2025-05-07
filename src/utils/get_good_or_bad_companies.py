from pandas import Series


def get_good_or_bad_companies(companies, scores, bad_threshold: int = 3) -> dict[str, dict[str, list[str]]]:
    if not isinstance(companies, Series) or not isinstance(scores, Series):
        raise TypeError("Companies and scores must be pandas Series")

    stats = { 'good': { 'companies': [], 'length': 0 }, 'bad': { 'companies': [], 'length': 0 } }
    for company, score in zip(companies, scores):
        if score > bad_threshold:
            stats['good']['companies'].append(company)
            stats['good']['length'] += 1
            continue
        stats['bad']['companies'].append(company)
        stats['bad']['length'] += 1
    return stats
