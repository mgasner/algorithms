var linear_search = function (arr, key) {
  for (var i = 0, len = arr.length; i < len; i++) {
    if (arr[i] === key) return i;
  }
  return "nil";
}