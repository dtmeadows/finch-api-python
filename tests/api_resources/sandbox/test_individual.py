# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.sandbox import IndividualUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestIndividual:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        individual = client.sandbox.individual.update(
            "string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        individual = client.sandbox.individual.update(
            "string",
            dob="12/20/1989",
            emails=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            encrypted_ssn="string",
            ethnicity="asian",
            first_name="string",
            gender="female",
            last_name="string",
            middle_name="string",
            phone_numbers=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            preferred_name="string",
            residence={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
                "name": "string",
                "source_id": "string",
            },
            ssn="string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.individual.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])


class TestAsyncIndividual:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncFinch) -> None:
        individual = await client.sandbox.individual.update(
            "string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncFinch) -> None:
        individual = await client.sandbox.individual.update(
            "string",
            dob="12/20/1989",
            emails=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            encrypted_ssn="string",
            ethnicity="asian",
            first_name="string",
            gender="female",
            last_name="string",
            middle_name="string",
            phone_numbers=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            preferred_name="string",
            residence={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
                "name": "string",
                "source_id": "string",
            },
            ssn="string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncFinch) -> None:
        response = await client.sandbox.individual.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])