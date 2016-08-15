from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
from IPython.core.display import display, HTML

quiz_id = 0

questionTemplate = """
<label>%s </label>
	  	 <input type="text" placeholder="0">
"""

@register_cell_magic
def quiz(line, cell):
    global quiz_id
    quiz_id += 1
    answers = eval(line)
    questions = cell.split("\n")
    totalQs = "".join([questionTemplate%question for question in questions])
    return HTML((ht%(totalQs,str(answers))).replace("QID",str(quiz_id)))



ht = """
<section>
	  <form id="formQID" class="input-list style-4 clearfix">
	  		%s
	  </form>
	  	  	 <button onclick="check(QID)">Check Answers</button>

	</section>
  <script>
  answersQID = %s;
  function check(num){
  	responses=[]
  	canswers = eval("answers"+num);
  	formNum = "#form"+num+" input"
  	$(formNum).each(function(i){
  		try {
  			value = math.parse($(this).val()).eval();
  			responses.push(value);
  			actualValue = canswers[i];
  			console.log([value,actualValue,i]);
  			if(Math.abs(value-actualValue) < .0001){
  				$(this).removeClass("incorrect-quiz").addClass("correct-quiz");
  			}
  			else {
  				$(this).addClass("incorrect-quiz").removeClass("correct-quiz");
  			}
  		}
  		catch(err){
  			$(this).addClass("incorrect-quiz").removeClass("correct-quiz");
  		}
  	});
  }

  </script>
  <style>
.style-4 input[type="text"] {
  display: block;
  margin: 0;
  font-family: sans-serif;
  font-size: 18px;
  appearance: none;
  box-shadow: none;
  border-radius: none;
  margin: 10px;
}
.style-4 input[type="text"]:focus {
  outline: none;
}

.style-4 input[type="text"] {
  padding: 10px;
  border: none;
  border-bottom: solid 2px #c9c9c9;
  transition: border 0.3s;
}
.style-4 input[type="text"]:focus,
.style-4 input[type="text"].focus {
  border-bottom: solid 2px #969696;
}

input[type=text].correct-quiz {
  border: solid 1px #125600; 
  box-shadow: 0 0 5px 1px #00840f;
}

input[type=text].incorrect-quiz {
  border: solid 1px #e61313; 
  box-shadow: 0 0 5px 1px #a81819;
}
  </style>
"""
