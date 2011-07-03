var maximum_subarray = function (arr, low, high) {
  if (high === low) {
    return {
      max_left: low,
      max_right: high,
      sum: arr[low]
    };
  } else {
    var mid = Math.floor((low + high) / 2);
    var left = maximum_subarray(arr, low, mid);
    var right = maximum_subarray(arr, mid, high);
    var cross = find_max_crossing_subarray(arr, low, mid, high);
    
    if ((left.sum >= right.sum) && (left.sum >= cross.sum)) {
      return left;
    } else if ((right.sum >= left.sum) && (right.sum >= cross.sum)) {
      return right;
    } else {
      return cross;
    }
  }
}

var find_max_crossing_subarray = function(arr, low, mid, high) {
  var left_sum = arr[mid];
  var right_sum = arr[mid];
  var max_left = mid;
  var max_right = mid;
  
  for (var i = mid, sum = 0; low <= i; i--) {
    sum = sum + arr[i];
    if (sum > left_sum) {
      left_sum = sum;
      max_left = i;
    }
  }
  
  for (var i = mid, sum = 0; high >= i; i++) {
    sum = sum + arr[i];
    if (sum > right_sum) {
      right_sum = sum;
      max_right = i;
    }
  }

  return {
    max_left: max_left,
    max_right: max_right,
    sum: left_sum + right_sum
  };
}