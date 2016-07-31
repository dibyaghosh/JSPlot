	(function () {
		var __symbols__ = ['e5'];
		var math = Math;
		var setup = function () {
			return 'lb';
		};
		var inputs = function () {
			return list ([list (['n', 0, 100, 5]), list (['p', 0, 1, 0.1])]);
		};
		var prob = function (n, p, x) {
			var q = 1 - p;
			var nx = n - x;
			return (jStat.combination (n, x) * Math.pow (p, x)) * Math.pow (q, nx);
		};
		var data = function (n, p) {
			var x = list (range (n + 1));
			var y = function () {
				var __accu0__ = [];
				var __iterable0__ = x;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (prob (n, p, i));
				}
				return __accu0__;
			} ();
			var y2 = function () {
				var __accu0__ = [];
				var __iterable0__ = x;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (jStat.normal.pdf (i, n * p, math.sqrt ((n * p) * (1 - p))));
				}
				return __accu0__;
			} ();
			bar2 (x, y);
			plot2 (x, y2);
		};
		__pragma__ ('<all>')
			__all__.data = data;
			__all__.inputs = inputs;
			__all__.math = math;
			__all__.prob = prob;
			__all__.setup = setup;
		__pragma__ ('</all>')
	}) ();
