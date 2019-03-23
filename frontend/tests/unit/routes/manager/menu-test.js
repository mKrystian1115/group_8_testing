import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | manager/menu', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:manager/menu');
    assert.ok(route);
  });
});
