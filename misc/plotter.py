import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_pies(tracker, curr):
    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]])

    # For incomes
    fig.add_trace(
        go.Pie(
            labels=tracker.incomes.Type,
            values=tracker.incomes.Amount,
            name="Incomes",
            title="Incomes",
            titleposition='top center',
            scalegroup="one"),
        row=1, col=1)

    # For expenses
    fig.add_trace(
        go.Pie(
            labels=tracker.expenses.Type,
            values=tracker.expenses.Amount,
            name="Expenses",
            title="Expenses",
            titleposition='top center',
            scalegroup="one"),
        row=1, col=2)

    # For investments
    fig.add_trace(
        go.Pie(
            labels=tracker.investments.Type,
            values=tracker.investments.Amount,
            name="Investments",
            title="Investments",
            titleposition='top center',
            scalegroup="one"),
        row=1, col=3)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+value+name")

    # Get totals data
    income = tracker.total_incomes()
    expense = tracker.total_expenses()
    investment = tracker.total_investments()

    fig.update_layout(
        title=dict(text="Plots for {} {}".format(tracker.month, tracker.year),
                   x=0.5,
                   xanchor='center',
                   font=dict(size=22)),
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=curr.format(income), x=0.12, y=0.5, font_size=20, showarrow=False),
                     dict(text=curr.format(expense), x=0.5, y=0.5, font_size=20, showarrow=False),
                     dict(text=curr.format(investment), x=0.88, y=0.5, font_size=20, showarrow=False)],
        template='none')
    fig.show()


def plot_bars(tracker):
    # Get totals
    income = tracker.total_incomes()
    expense = tracker.total_expenses()
    investment = tracker.total_investments()

    # Generate data
    types = ["Income", "Expense", "Investment"]
    values = [income, expense, investment]

    fig = go.Figure([go.Bar(x=types, y=values, text=values, textposition='auto')])
    fig.show()
