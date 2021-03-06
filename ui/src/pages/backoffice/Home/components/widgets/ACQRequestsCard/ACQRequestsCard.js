import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Loader, Error } from '@components';
import { RecordsBriefCard } from '@pages/backoffice/components/statistics/RecordsBriefCard';
import { NewButton, SeeAllButton } from '@pages/backoffice/components/buttons';

export default class ACQRequestsCard extends Component {
  constructor(props) {
    super(props);

    // TODO when acquisition module
    this.seeAllUrl = '';
    this.newAcqURL = '';
  }

  componentDidMount() {}

  seeAllButton = () => {
    return <SeeAllButton fluid disabled to={this.seeAllUrl} />;
  };

  newAcqButton = () => {
    return <NewButton fluid disabled to={this.newAcqURL} />;
  };

  renderCard = data => {
    return (
      <RecordsBriefCard
        title={'ACQ Requests'}
        stats={data}
        text={'ongoing'}
        buttonLeft={this.newAcqButton()}
        buttonRight={this.seeAllButton()}
      />
    );
  };

  render() {
    const { data, isLoading, error } = this.props;
    return (
      <Loader isLoading={isLoading}>
        <Error error={error}>{this.renderCard(data)}</Error>
      </Loader>
    );
  }
}

ACQRequestsCard.propTypes = {
  // fetchOngoingAcqRequests: PropTypes.func.isRequired,
  data: PropTypes.number.isRequired,
};
