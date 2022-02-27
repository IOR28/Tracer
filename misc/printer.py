from IPython.display import display, HTML


def print_title(tracker):
    title = "{} {}".format(tracker.month, tracker.year)

    display(HTML('<h1 style="text-align:center">' + title + '</h1>'))


def print_results(tracker, curr):
    title = "Results for {} {}".format(tracker.month, tracker.year)

    text = ""
    text += "The total amount earned is " + curr.format(tracker.total_incomes()) + '<br>'
    text += "The total amount spent is " + curr.format(tracker.total_expenses()) + '<br>'
    text += "The balance this month is " + curr.format(tracker.balance()) + '<br>'
    text += "The total amount invested is " + curr.format(tracker.total_investments()) + '<br>'

    display(HTML('<h3 style="text-align:center">' + title + '</h3>'))
    display(HTML('<p style="text-align:center">' + text + '</p>'))
