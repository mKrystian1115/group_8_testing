import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({
  model(params) {
    return RSVP.hash({
      tickets: this.store.findRecord("ticket", params.ticket_id),
      prices: this.store.findRecord("price", 1)
    });
  }
});
