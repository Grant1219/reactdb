<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <title>ReactDB</title>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
        <meta name="keywords" content="reactdb reaction image database" />
        <meta name="description" content="reactdb reaction image database" />
        <link rel="shortcut icon" href="${request.static_url ('reactdb:static/favicon.ico')}" />
        <link rel="stylesheet" href="${request.static_url ('reactdb:static/style.css')}" type="text/css" media="screen" charset="utf-8" />
    </head>
    <body>
        <h1>ReactDB</h1>
        <div id="reactdb_search">
            <form id="reactdb_search_form" action="" method="get">
                %if 'query' in request.GET:
                <p><input type="text" name="query" value="${request.GET['query']}" /></p>
                %else:
                <p><input type="text" name="query" /></p>
                %endif
            </form>
        </div>
        <div id="reactdb_results">
            % if images is not None:
            % for image in images:
            <a href="${request.static_url ('reactdb:static/images/%s' % image.filename)}"><img class="reactdb_image" src="${request.static_url ('reactdb:static/images/%s' % image.filename)}" /></a>
            % endfor
            % else:
            <p>Your search did not match any images.</p>
            % endif
        </div>
    </body>
</html>
