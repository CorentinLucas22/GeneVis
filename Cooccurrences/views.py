from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from .models import Abbreviations, Cells, Chemicals, Dates, Diseases, Enzymes, Genes, Histones, Mutations, Species, Tissues

# Chaque fonction de ce fichier permet de charger un template html, qui en conbinaison avec urls.py permet
# de charger une page à une url définie dans urls.py


def index_view(request):
    # View returning /genevis/ url

    return render(request, 'Cooccurrences/index.html',)
    # 'Cooccurrences/index.html' refers to the path to the template
    #  which is index.html located in the Cooccurrences folder.


def request_view(request):
    # View returning /genevis/request/ url

    return render(request, 'Cooccurrences/request.html')


def result_view(request):

    if request.method == "GET":
        # method=="GET" as the request does not need to do any modification in our system.
        t1 = request.GET["t1"]  # table1
        t2 = request.GET["t2"]  # table2
        f1 = request.GET["f1"]  # field1
        f2 = request.GET["f2"]  # field2
        source = request.GET["Source entity"]
        target = request.GET["Target entity"]
        # these are the values that are put by the user in the query card,
        # t1 is the choice of the first table, source is the text written in the field.

        # Checking if the user didn't put the same table in both fields :
        if t1 == t2:
            wrong_table = "This site is made to conduct your request on two different tables, \
                    your request had the source and the target table being the same table %s=%s. please use two different tables." % (t1, t2)
            wrong_table_dict = {
                'wrong_table': wrong_table,
            }
            return render(request, 'Cooccurrences/error.html', wrong_table_dict)

        # These ifs are there in order to chose which model will be used to perform the query.
        if t1 == "abbreviations":
            SQL_class = Abbreviations
        elif t1 == "cells":
            SQL_class = Cells
        elif t1 == "chemicals":
            SQL_class = Chemicals
        elif t1 == "dates":
            SQL_class = Dates
        elif t1 == "diseases":
            SQL_class = Diseases
        elif t1 == "enzymes":
            SQL_class = Enzymes
        elif t1 == "genes":
            SQL_class = Genes
        elif t1 == "histones":
            SQL_class = Histones
        elif t1 == "mutations":
            SQL_class = Mutations
        elif t1 == "species":
            SQL_class = Species
        elif t1 == "tissues":
            SQL_class = Tissues

        # These ifs follow the same logic, but will be used to display the matching elements.
        if t2 == "abbreviations":
            Matching_class = Abbreviations
        elif t2 == "cells":
            Matching_class = Cells
        elif t2 == "chemicals":
            Matching_class = Chemicals
        elif t2 == "dates":
            Matching_class = Dates
        elif t2 == "diseases":
            Matching_class = Diseases
        elif t2 == "enzymes":
            Matching_class = Enzymes
        elif t2 == "genes":
            Matching_class = Genes
        elif t2 == "histones":
            Matching_class = Histones
        elif t2 == "mutations":
            Matching_class = Mutations
        elif t2 == "species":
            Matching_class = Species
        elif t2 == "tissues":
            Matching_class = Tissues

        # End of model check.

        # Verification if the field selected by the user exists in the selected table.
        # If it doesnt exists then the user is redirected towards an error page which will
        # tell him his error and allow him to reconduct his query.
        if t1 in ("abbreviations", "cells", "chemicals", "diseases", "enzymes", "genes", "histones", "tissues"):
            if f1 not in ("pmid", "normalized", "entity"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f1, t1),
                })

        if t1 == ("mutations"):
            if f1 not in ("pmid", "vartype", "normalized", "entity"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f1, t1),
                })

        if t1 == ("species"):
            if f1 not in ("pmid", "probability", "normalized", "entity"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f1, t1),
                })

        if t1 == ("dates"):
            if f1 not in ("pmid", "pubYear", "pubMonth", "pubDay"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f1, t1),
                })

        if t2 in ("abbreviations", "cells", "chemicals", "diseases", "enzymes", "genes", "histones", "tissues"):
            if f2 not in ("pmid", "normalized", "entity"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f2, t2),
                })

        if t2 == ("mutations"):
            if f2 not in ("pmid", "vartype", "normalized", "entity"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f2, t2),
                })

        if t2 == ("species"):
            if f2 not in ("pmid", "probability", "normalized", "entity"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f2, t2),
                })

        if t2 == ("dates"):
            if f2 not in ("pmid", "pubYear", "pubMonth", "pubDay"):
                return render(request, 'Cooccurrences/error.html', {
                    'error_message': "The field %s does not exist in the %s table, please refer to table's model."
                    % (f2, t2),
                })
        # End of verifications.

    # * IF YOU WISH TO MODIFY THE PARAMETERS OF THE SQL QUERIES YOU CAN MODIFY THE STRING CONTAINED IN results
    # These requests have the goal of retrieving the data sharing the same pmid between t1 and t2.
    # This is done with the 1st and 2nd lines in the SQL request.
    # Then the WHERE clause allows the request to apply filters to find biological entities or dates.
    # It is worth noting that when using either the "dates" table or the "normalized" field
    # we do not want to use a LIKE as we would get data that is not what we are looking for.
    # * Modify the LIKE clause by removing some % wildcards if you wish to change how the filter is done.

    # matches is the reverse query of results, allowing the display of the matching entities in result.html

    # Variable used to check if t2 == dates in result.html
    is_date = 0

    if t1 == "dates" and f2 == "normalized":
        # ? this is an SQL request
        results = SQL_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s LIKE '%s%s%s' AND %s.%s = '%s';"
            % (t1, t2, f2, t1, t2, t1, t2, t1, f1, '%%', source, '%%', t2, f2, target,)
        )

        # ? this is an SQL request
        matches = Matching_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s = '%s' AND %s.%s LIKE '%s%s%s';"
            % (t2, t1, f1, t2, t1, t2, t1, t2, f2, target, t1, f1, '%%', source, '%%',)
        )

    elif t2 == ("dates"):
        is_date = 1

        # ? this is an SQL request
        if f1 == "normalized":
            results = SQL_class.objects.raw(
                "SELECT %s.*, %s.%s FROM %s \
                INNER JOIN %s ON %s.pmid = %s.pmid \
                WHERE %s.%s = '%s' AND %s.%s LIKE '%s%s%s';"
                % (t1, t2, f2, t1, t2, t1, t2, t1, f1, source, t2, f2, '%%', target, '%%',)
            )

            # ? this is an SQL request
            matches = Matching_class.objects.raw(
                "SELECT %s.*, %s.%s FROM %s \
                INNER JOIN %s ON %s.pmid = %s.pmid \
                WHERE %s.%s LIKE '%s%s%s' AND %s.%s = '%s';"
                % (t2, t1, f1, t2, t1, t2, t1, t2, f2, '%%', target, '%%', t1, f1, source,)
            )

        else:
            # ? this is an SQL request
            results = SQL_class.objects.raw(
                "SELECT %s.*, %s.%s FROM %s \
                INNER JOIN %s ON %s.pmid = %s.pmid \
                WHERE %s.%s LIKE '%s%s%s' AND %s.%s LIKE '%s%s%s';"
                % (t1, t2, f2, t1, t2, t1, t2, t1, f1, '%%', source, '%%', t2, f2, '%%', target, '%%',)
            )

            # ? this is an SQL request
            matches = Matching_class.objects.raw(
                "SELECT %s.*, %s.%s FROM %s \
                INNER JOIN %s ON %s.pmid = %s.pmid \
                WHERE %s.%s LIKE '%s%s%s' AND %s.%s LIKE '%s%s%s';"
                % (t2, t1, f1, t2, t1, t2, t1, t2, f2, '%%', target, '%%', t1, f1, '%%', source, '%%',)
            )

    # These ones are in the case of searching for a normalized name, if we input 1437 as normalized we don't want any normalized = 1437X
    elif f1 == "normalized" and f2 != "normalized":
        # ? this is an SQL request
        results = SQL_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid=%s.pmid \
            WHERE %s.%s = '%s' AND %s.%s LIKE '%s%s%s'"
            % (t1, t2, f2, t1, t2, t1, t2, t1, f1, source, t2, f2, '%%', target, '%%',)
        )

        # ? this is an SQL request
        matches = Matching_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid=%s.pmid \
            WHERE %s.%s LIKE '%s%s%s' AND %s.%s = '%s'"
            % (t2, t1, f1, t2, t1, t2, t1, t2, f2, '%%', target, '%%', t1, f1, source,)
        )

    elif f2 == "normalized" and f1 != "normalized":
        # ? this is an SQL request
        results = SQL_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s LIKE '%s%s%s' AND %s.%s = '%s';"
            % (t1, t2, f2, t1, t2, t1, t2, t1, f1, '%%', source, '%%', t2, f2, target,)
        )

        # ? this is an SQL request
        matches = Matching_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s = '%s' AND %s.%s LIKE '%s%s%s';"
            % (t2, t1, f1, t2, t1, t2, t1, t2, f2, target, t1, f1, '%%', source, '%%',)
        )

    elif f1 == "normalized" and f2 == "normalized":
        # ? this is an SQL request
        results = SQL_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s = %s AND %s.%s = %s;"
            % (t1, t2, f2, t1, t2, t1, t2, t1, f1, source, t2, f2, target,)
        )

        # ? this is an SQL request
        matches = Matching_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s LIKE '%s%s%s' AND %s.%s LIKE '%s%s%s';"
            % (t2, t1, f1, t2, t1, t2, t1, t2, f2, '%%', target, '%%', t1, f1, '%%', source, '%%',)
        )

    else:
        # ? this is an SQL request
        results = SQL_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s LIKE '%s%s%s' AND %s.%s LIKE '%s%s%s';"
            % (t1, t2, f2, t1, t2, t1, t2, t1, f1, '%%', source, '%%', t2, f2, '%%', target, '%%',)
        )

        # ? this is an SQL request
        matches = Matching_class.objects.raw(
            "SELECT %s.*, %s.%s FROM %s \
            INNER JOIN %s ON %s.pmid = %s.pmid \
            WHERE %s.%s LIKE '%s%s%s' AND %s.%s LIKE '%s%s%s';"
            % (t2, t1, f1, t2, t1, t2, t1, t2, f2, '%%', target, '%%', t1, f1, '%%', source, '%%',)
        )

    #  * Exemple d'une requête :
    #  ? SELECT genes.*, species.entity FROM genes
    #  ? INNER JOIN species ON species.pmid = genes.pmid
    #  ? WHERE genes.entity LIKE '%myosin%' AND species.entity LIKE '%fish%';

    # a bit of a trick to display the correct match for the result.html template
    # because of the not very practical loop structure for django template loops,
    # (no access to an index, no break, making it very tricky to properly handle
    # nested loops... ended up building an index myself).
    for i in range(len(results)):
        results[i].id = i+1

    # * Dictionary containing all the data retrieved by the SQL request that was
    # * used during the call of this view.
    context = {
        'results': results,
        'matches': matches,
        "is_date": is_date,
    }

    return render(request, 'Cooccurrences/result.html', context)


def about_view(request):

    return render(request, 'Cooccurrences/about.html')
