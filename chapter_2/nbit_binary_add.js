var nbit_binary_add = function (a, b) {
  var carry = 0;
  var c = [];
  var n = a.length
  for (var i = 0; i < n; i++) {
    if (a[i]) {
      if (b[i]) {
        if (carry) {
          c[i] = 1;
        } else {
          c[i] = 0;
          carry = 1;
        }
      } else {
        if (carry) {
          c[i] = 0;
        } else {
          c[i] = 1;
        }
      }
    } else {
      if (b[i]) {
        if (carry) {
          c[i] = 0;
        } else {
          c[i] = 1;
        }
      } else {
        if (carry) {
          c[i] = 1;
          carry = 0;
        } else {
          c[i] = 0;
        }
      }
    }
  }
  if (carry) {
    c[n] = 1;
  }
  return c;
}