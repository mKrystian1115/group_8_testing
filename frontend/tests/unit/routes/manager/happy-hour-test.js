import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | manager/happy-hour', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:manager/happy-hour');
    assert.ok(route);
  });
});
