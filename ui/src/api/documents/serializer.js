import isEmpty from 'lodash/isEmpty';
import { fromISO } from '../date';

function serializeResponse(hit) {
  let result = {};
  if (!isEmpty(hit)) {
    result['id'] = hit.id;
    result['created'] = fromISO(hit.created);
    result['updated'] = fromISO(hit.updated);
    if (hit.links) {
      result['links'] = hit.links;
    }
    if (!isEmpty(hit.metadata)) {
      result['metadata'] = hit.metadata;
      if (!isEmpty(hit.metadata.circulation.next_available_date)) {
        result['metadata']['circulation']['next_available_date'] = new Date(
          result['metadata']['circulation']['next_available_date']
        ).toDateString();
      }
      result['pid'] = hit.metadata.pid;
    }
    if (!isEmpty(hit.metadata.imprint)) {
      hit.metadata.imprint.date = hit.metadata.imprint.date
        ? fromISO(hit.metadata.imprint.date)
        : null;
    }
  }
  return result;
}

export const serializer = {
  fromJSON: serializeResponse,
};
