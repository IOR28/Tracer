import io
import nbformat


def execute_notebook(name, print_tables=False, print_results=False, print_graphs=False):
    nbfile = name + ".ipynb"
    try:
        with io.open(nbfile) as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)

        ip = get_ipython()

        i = 1  # avoid cell 0, imports
        while i < 5:
            cell = nb.cells[i]
            if cell.cell_type != 'code':
                continue
            ip.run_cell(cell.source)
            i += 1

        if print_tables:  # 3 tables, one cell each
            while i < 8:
                cell = nb.cells[i]
                if cell.cell_type != 'code':
                    continue
                ip.run_cell(cell.source)
                i += 1

        if print_results:  # Eigth cell contains results
            i = 8
            cell = nb.cells[i]
            ip.run_cell(cell.source)

        if print_graphs:
            # ToDo
            pass

    except IOError:
        print("There is no {} notebook.".format(nbfile))

    return


def execute_tracker_month(year, month, print_tables=False, print_results=False, print_graphs=False):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    name = "./{}/{}_{}".format(year, month, months[month - 1])
    execute_notebook(name, print_tables, print_results, print_graphs)

    return
