


String.prototype.includes = function(substring) {
  return this.indexOf(substring) > 0;
};

Array.prototype.sortByProperty = function(propertyName, descending = false) {

  function compare(a,b) {
    if (a[propertyName] < b[propertyName])
      return 1;
    if (a[propertyName] > b[propertyName])
      return -1;
    return 0;
  }

  this.sort(compare);

  if (descending) {
    this.reverse();
  }

  return this;

};

Array.prototype.findByProperty = function(property, value) {
  return this.find(function(item) { return item[property] == value; });
};
