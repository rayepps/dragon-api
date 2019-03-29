


function TemplateService() {

    this.name = 'TemplateService';

    var $templates = $('script[type="text/x-template"]');
    this.templates = {};
    var self = this;
    $templates.each(function(i, elem) {
      var $template = $(elem);
      var templateName = $template.data('template-name');
      self.templates[templateName] = $template.html();
    });
}

TemplateService.prototype.template = function(templateName, data) {
  if (this.templates.hasOwnProperty(templateName)) {
    // TODO: actually template
    return this._template(this.templates[templateName], data);
  } else {
    console.error(templateName + ' could not be found');
    return null;
  }
};

TemplateService.prototype._template = function(template, data) {
  var re = /\{\{\s(.+?)\s\}\}/g;

  var t = template.replace(re, function(match, varName, pos) {
    return data[varName];
  });

  return t;
};
