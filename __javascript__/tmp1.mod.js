	(function () {
		var __symbols__ = ['e5'];
		var math = Math;
		var setup = function () {
			return 'l';
		};
		var inputs = function () {
			return list ([list (['x', 0, 10, 1])]);
		};
		var data = function (x) {
			var r = list (range (x));
			var y = function () {
				var __accu0__ = [];
				var __iterable0__ = r;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (math.pow (i, 2));
				}
				return __accu0__;
			} ();
			plot1 (r, y);
			console.log (y);
			bar1 (r, r);
		};
		__pragma__ ('<all>')
			__all__.data = data;
			__all__.inputs = inputs;
			__all__.math = math;
			__all__.setup = setup;
		__pragma__ ('</all>')
	}) ();
