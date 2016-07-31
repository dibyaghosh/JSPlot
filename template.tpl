{% extends 'full.tpl'%}

{% block header %}
{{ super() }}
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{% endblock header %}
{% block input_group %}
    <div class="panel-group">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" href="#collapse{{cell['execution_count']}}">Code</a>
      </h4>
    </div>
    <div id="collapse{{cell['execution_count']}}" class="panel-collapse collapse {% if cell.metadata.get('show',False) %} in {% endif %}">
              {{ super() }}
    </div>
  </div>
</div>
{% endblock input_group %}