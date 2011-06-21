var horners_rule = function (coeffs, x) {
  var y = 0;
  for (var i = coeffs.length; i > 0; i--) {
    y = coeffs[i - 1] + (x * y);
  }
  return y;
}