
function DragonModule(services) {

  this.services = services || [];

  var views = $('[data-controller]');

  views.each(function(i, elem) {
    var $view = $(elem);
    var controllerName = $view.data('controller');
    if (window.hasOwnProperty(controllerName)) {
      var args = $view.data('controller-args');
      var controller = new window[controllerName]($view, this.services, args);
    } else {
      console.error(controllerName + ' could not be found');
    }

  }.bind(this));

}
