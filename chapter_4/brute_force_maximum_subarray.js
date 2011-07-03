var brute_force_subarray = function (arr) {
  var left, right = 0;
  var max = arr[0];

  for (var i = 0; i < arr.length; i++) {
    for (var j = i + 1; j < arr.length; j++) {
      var sum = arr[i];
      for (var k = i + 1; k < j; k++) {
        sum = sum + arr[k];
      }
      if (sum > max) {
        max = sum;
        left = i;
        right = j;
      }
    }
  }
  
  return {
    left: left,
    right: right,
    sum: max
  };
}