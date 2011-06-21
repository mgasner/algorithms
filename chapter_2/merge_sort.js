var merge_sort = function (arr) {

  var merge = function (arr, p, q, r) {
    var left = [];
    var right = [];

    for (var i = 0; p + i <= q; i++) {
      left[i] = arr[p + i];
    }
    for (var j = 0; q + 1 + j <= r; j++) {
      right[j] = arr[q + 1 + j];
    }
    left[i] = Math.exp(1000);
    right[j] = Math.exp(1000);
    
    i = 0;
    j = 0;
    for (var k = p; k <= r; k++) {
      if (left[i] < right[j]) {
        arr[k] = left[i];
        i++;
      } else {
        arr[k] = right[j];
        j++;
      }
    }
  }

  var merge_sort_helper = function (arr, p, r) {
    if (p < r) {
      var q = Math.floor((p + r) / 2);
      merge_sort_helper(arr, p, q);
      merge_sort_helper(arr, q + 1, r);
      merge(arr, p, q, r);
    }
  }
 
  merge_sort_helper(arr, 0, arr.length - 1)
  return arr;
}

var merge = function(arr, p, q, r) {
  
  
  
  
  return arr;
}