	(function () {
		var __symbols__ = ['e5'];
		var math = Math;
		var setup = function () {
			return 'b';
		};
		var inputs = function () {
			return list ([list (['mu', 0, 10, 1])]);
		};
		var factorial = function (x) {
			var i = 1;
			for (var _ = 1; _ < x + 1; _++) {
				i *= _;
			}
			return i;
		};
		var prob = function (mu, x) {
			return (math.pow (math.E, -(1) * mu) * math.pow (mu, x)) / factorial (x);
		};
		var data = function (mu) {
			var x = list (range (4 * mu));
			var y = function () {
				var __accu0__ = [];
				var __iterable0__ = x;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (prob (mu, i));
				}
				return __accu0__;
			} ();
			write (3, 'Hi');
			bar (3, x, y);
		};
		__pragma__ ('<all>')
			__all__.data = data;
			__all__.factorial = factorial;
			__all__.inputs = inputs;
			__all__.math = math;
			__all__.prob = prob;
			__all__.setup = setup;
		__pragma__ ('</all>')
	}) ();
