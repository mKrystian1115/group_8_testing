import DS from 'ember-data';

export default DS.Model.extend({
  start: DS.attr(),
  duration: DS.attr(),
  numplate: DS.attr(),
  paid: DS.attr()
});
