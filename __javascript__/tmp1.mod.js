	(function () {
		var __symbols__ = ['e5'];
		var math = Math;
		var setup = function () {
			return 'l';
		};
		var inputs = function () {
			return list ([list (['Beginning Range', 0, 100, 5]), list (['End of Range', 10, 100, 5])]);
		};
		var data = function (down, up) {
			if (down >= up) {
				var down = 0;
			}
			var p = 1;
			var x = list ([1]);
			var y = list ([0]);
			for (var i = 0; i < up; i++) {
				p *= (366 - i) / 365;
				x.append (i);
				y.append (1 - p);
			}
			plot (1, x.__getslice__ (down, null, 1), y.__getslice__ (down, null, 1));
			write (1, (('The probability that two people share a birthday in a room with ' + str (up)) + ' people is ') + str (y [len (y) - 1]));
		};
		__pragma__ ('<all>')
			__all__.data = data;
			__all__.inputs = inputs;
			__all__.math = math;
			__all__.setup = setup;
		__pragma__ ('</all>')
	}) ();
