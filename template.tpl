{% extends 'full.tpl'%}

{% block body %}
<!--
<header class="main-header post-head " style="background-image: url(http://www.casinonewsdaily.com/wp-content/uploads/guides/illustrations/roulette/basics/roulette-wheel.jpg)">
</header> -->
{{ super() }}
{% endblock body %}


{% block header %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/3.3.0/math.min.js"></script>
{{ super() }}
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<script src="https://ajaxorg.github.io/ace-builds/src-min-noconflict/ace.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

{% endblock header %}




{% block input_group %}
    <div class="panel-group">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" href="#collapse{{cell['execution_count']}}">Code</a>
        <a onclick="ace.edit('code{{cell['execution_count']}}').getSession().setMode('ace/mode/python')">Edit</a>
      </h4>
    </div>
    <div id="collapse{{cell['execution_count']}}" class="panel-collapse collapse {% if cell.metadata.get('show',False) %} in {% endif %}">
    <div id="code{{cell['execution_count']}}" style="max-height:300px">def f(x): return 1+1 </div>
              {{ super() }}
    </div>
  </div>
</div>
{% endblock input_group %}