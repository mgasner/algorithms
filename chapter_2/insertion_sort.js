var insertion_sort = function (arr) {
  for (var i = 0, len = arr.length; i < len; i++) {
    var j = i;
    while (j > 0 && arr[j] < arr[j-1]) {
      var x = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = x;
      j--;
    }
  }
  return arr;
}