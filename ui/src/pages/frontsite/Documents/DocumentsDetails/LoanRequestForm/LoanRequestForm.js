import React, { Component } from 'react';
import { Button, Checkbox, Form } from 'semantic-ui-react';
import { Error } from '@components/Error';
import { DatePicker } from '@components';
import PropTypes from 'prop-types';
import { invenioConfig } from '@config';
import { DateTime } from 'luxon';
import { toShortDate } from '@api/date';
import isEmpty from 'lodash/isEmpty';

export default class LoanRequestForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      requestEndDate: '',
      deliveryMethod: '',
    };

    // init delivery method
    this.withDeliveryMethod = !isEmpty(
      invenioConfig.circulation.deliveryMethods
    );
    this.deliveryMethods = this.withDeliveryMethod
      ? Object.keys(invenioConfig.circulation.deliveryMethods).map(key => ({
          key: key,
          value: key,
          text: invenioConfig.circulation.deliveryMethods[key],
        }))
      : [];
    this.state['deliveryMethod'] = this.withDeliveryMethod
      ? this.deliveryMethods[0].value
      : null;
  }

  requestLoanButton = () => {
    return (
      <Button
        positive
        size="small"
        content="Request"
        onClick={this.requestLoan}
      />
    );
  };

  handleRequestEndDateChange = value => {
    this.setState({ requestEndDate: value });
  };

  handleDeliveryMethodChange = (_, { value }) => {
    this.setState({ deliveryMethod: value });
  };

  handleSubmit = () => {
    const documentPid = this.props.document.metadata.pid;
    const optionalParams = {};
    if (!isEmpty(this.state.requestEndDate)) {
      optionalParams.requestEndDate = this.state.requestEndDate;
    }
    if (!isEmpty(this.state.deliveryMethod)) {
      optionalParams.deliveryMethod = this.state.deliveryMethod;
    }
    this.props.requestLoanForDocument(documentPid, optionalParams);
  };

  renderDeliveryRadioButtons = () => {
    return this.deliveryMethods.map(method => (
      <Checkbox
        radio
        label={method.text}
        name={'deliveryMethodRadioGroup'}
        value={method.value}
        checked={this.state.deliveryMethod === method.value}
        onChange={this.handleDeliveryMethodChange}
        key={method.value}
      />
    ));
  };

  renderDeliveryMethodSelector = () => {
    return this.withDeliveryMethod ? (
      <>
        <Form.Field required>
          <label>I would like to</label>
        </Form.Field>
        <Form.Field>{this.renderDeliveryRadioButtons()}</Form.Field>
      </>
    ) : null;
  };

  renderOptionalRequestExpirationDate = () => {
    const today = DateTime.local();
    const initialDate = new DateTime(today.plus({ days: 10 }));
    const max = new DateTime(
      today.plus({ days: invenioConfig.circulation.requestDuration })
    );
    return (
      <Form.Field>
        <label>Do you require it before a certain date? (optional)</label>
        <DatePicker
          initialDate={toShortDate(initialDate)}
          minDate={toShortDate(today)}
          maxDate={toShortDate(max)}
          placeholder="Pick the date"
          handleDateChange={this.handleRequestEndDateChange}
        />
      </Form.Field>
    );
  };

  render() {
    const { error } = this.props;
    return (
      <Error error={error}>
        <Form>
          {this.renderDeliveryMethodSelector()}
          {this.renderOptionalRequestExpirationDate()}
          <Form.Button primary fluid onClick={this.handleSubmit}>
            Request
          </Form.Button>
        </Form>
      </Error>
    );
  }
}

LoanRequestForm.propTypes = {
  requestLoanForDocument: PropTypes.func.isRequired,
  document: PropTypes.object.isRequired,
};
