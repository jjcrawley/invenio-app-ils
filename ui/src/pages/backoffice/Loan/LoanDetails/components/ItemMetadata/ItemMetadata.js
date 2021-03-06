import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Button,
  Container,
  Grid,
  Header,
  Icon,
  Table,
} from 'semantic-ui-react';
import { invenioConfig } from '@config';

export default class ItemMetadata extends Component {
  getTitle(loanState) {
    const isRequest = invenioConfig.circulation.loanRequestStates.includes(
      loanState
    );
    const isActiveLoan = invenioConfig.circulation.loanActiveStates.includes(
      loanState
    );
    let title = 'Item for this loan';
    if (isRequest) {
      title = 'Assigned item for this request';
    } else if (isActiveLoan) {
      title = 'Item currently on loan';
    }
    return title;
  }

  render() {
    const { item, loanState, changeItemClickHandler } = this.props;
    return (
      <Grid className="item-metadata" padded columns={2}>
        <Grid.Column width={16}>
          <Header as="h1">
            {this.getTitle(loanState)}
            {invenioConfig.circulation.loanActiveStates.includes(loanState) && (
              <Button
                primary
                floated="right"
                size="small"
                onClick={() => changeItemClickHandler()}
              >
                <Icon name="exchange" />
                change item
              </Button>
            )}
          </Header>
        </Grid.Column>

        <Grid.Column>
          <Table basic="very" definition className="metadata-table">
            <Table.Body>
              <Table.Row>
                <Table.Cell width={4}>Item ID</Table.Cell>
                <Table.Cell width={12}>{item.pid}</Table.Cell>
              </Table.Row>
              <Table.Row>
                <Table.Cell>Barcode</Table.Cell>
                <Table.Cell>{item.barcode}</Table.Cell>
              </Table.Row>
              <Table.Row>
                <Table.Cell>Medium</Table.Cell>
                <Table.Cell>{item.medium}</Table.Cell>
              </Table.Row>
            </Table.Body>
          </Table>
        </Grid.Column>

        <Grid.Column>
          <Container>
            <Header as="h4">Description</Header>
            <p>{item.description}</p>
          </Container>
        </Grid.Column>
      </Grid>
    );
  }
}

ItemMetadata.propTypes = {
  item: PropTypes.object.isRequired,
  changeItemClickHandler: PropTypes.func.isRequired,
};
