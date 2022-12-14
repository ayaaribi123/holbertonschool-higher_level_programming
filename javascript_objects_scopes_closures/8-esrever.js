#!/usr/bin/node
exports.esrever = function (list) {
  const resualt = [];
		let i = 0;
		for (i; i = list.length; i++) {
			resualt.push(list.pop());
	}
	return resualt;
};
