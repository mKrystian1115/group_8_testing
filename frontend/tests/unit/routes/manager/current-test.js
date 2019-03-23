import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | manager/current', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:manager/current');
    assert.ok(route);
  });
});
