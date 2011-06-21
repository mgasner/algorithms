var selection_sort = function(arr) {  
  var smallest = function(arr, a, b) {
    var s = a;
    for (var i = a + 1; i < b; i++) {
      if (arr[i] < arr[s]) {
        s = i;
      }
    }
    return s;
  }

  for (var i = 0, len = arr.length; i < len - 1; i++) {
    var j = smallest(arr, i, len);
    var x = arr[j];
    arr[j] = arr[i];
    arr[i] = x;
  }
  
  return arr;

}