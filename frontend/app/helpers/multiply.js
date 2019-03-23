import { helper } from '@ember/component/helper';

export function multiply(a) {
  return a[0] * a[1];
}

export default helper(multiply);
