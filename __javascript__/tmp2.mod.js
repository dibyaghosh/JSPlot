	(function () {
		var __symbols__ = ['e5'];
		var math = Math;
		var setup = function () {
			return 'l';
		};
		var inputs = function () {
			return list ([list (['x', 0, 0.4, 0.01])]);
		};
		var linspace = function (start, end, num) {
			var spacing = (end - start) / num;
			return function () {
				var __accu0__ = [];
				for (var i = 0; i < num; i++) {
					__accu0__.append (start + spacing * i);
				}
				return __accu0__;
			} ();
		};
		var data = function (off) {
			var x = linspace (1 - 3 * off, 1 + 3 * off, 100);
			var y = function () {
				var __accu0__ = [];
				var __iterable0__ = x;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (math.log (i));
				}
				return __accu0__;
			} ();
			var xp = list ([1 - off, 1 - off, 1]);
			var yp = list ([math.log (1 - off), off / -(1000), off / -(1000)]);
			plot (2, x, y);
			plot (2, xp, yp);
			var angle = (math.atan (math.log (1 - off) / -(off)) * 180) / math.PI;
			write (2, ('The angle is ' + angle.toFixed (3)) + ' degrees');
			write (2, 'The slope of the line is ' + 1 / (1 - off));
		};
		__pragma__ ('<all>')
			__all__.data = data;
			__all__.inputs = inputs;
			__all__.linspace = linspace;
			__all__.math = math;
			__all__.setup = setup;
		__pragma__ ('</all>')
	}) ();
