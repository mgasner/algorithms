var range = function (n) {
  r = [];
  
  for (var i = 0; i < n; i++) {
    r[i] = i;
  }
  
  return r;
}

var basic_test_harness = function (n, f1, f2) {
  var ret = { n: [], f1: [], f2: []};
  for (var i = 0; i < n; i++) {
    r = range(i);
    t1 = time_function_application(f1, [r]);
    t2 = time_function_application(f2, [r]);
    ret.n[i] = i;
    ret.f1[i] = t1;
    ret.f2[i] = t2;
  }
  return ret;
}

var time_function_application = function (fun, args) {
  var start = new Date()
  fun.apply(undefined, args);
  var end = new Date()
  return end - start;
}