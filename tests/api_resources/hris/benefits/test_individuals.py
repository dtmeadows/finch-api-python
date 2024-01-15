# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.pagination import SyncSinglePage, AsyncSinglePage
from finch.types.hris.benefits import (
    IndividualBenefit,
    EnrolledIndividual,
    UnenrolledIndividual,
    IndividualEnrolledIDsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestIndividuals:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_enroll_many(self, client: Finch) -> None:
        individual = client.hris.benefits.individuals.enroll_many(
            "string",
            individuals=[{}],
        )
        assert_matches_type(SyncSinglePage[EnrolledIndividual], individual, path=["response"])

    @parametrize
    def test_raw_response_enroll_many(self, client: Finch) -> None:
        response = client.hris.benefits.individuals.with_raw_response.enroll_many(
            "string",
            individuals=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(SyncSinglePage[EnrolledIndividual], individual, path=["response"])

    @parametrize
    def test_streaming_response_enroll_many(self, client: Finch) -> None:
        with client.hris.benefits.individuals.with_streaming_response.enroll_many(
            "string",
            individuals=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = response.parse()
            assert_matches_type(SyncSinglePage[EnrolledIndividual], individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_enrolled_ids(self, client: Finch) -> None:
        individual = client.hris.benefits.individuals.enrolled_ids(
            "string",
        )
        assert_matches_type(IndividualEnrolledIDsResponse, individual, path=["response"])

    @parametrize
    def test_raw_response_enrolled_ids(self, client: Finch) -> None:
        response = client.hris.benefits.individuals.with_raw_response.enrolled_ids(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(IndividualEnrolledIDsResponse, individual, path=["response"])

    @parametrize
    def test_streaming_response_enrolled_ids(self, client: Finch) -> None:
        with client.hris.benefits.individuals.with_streaming_response.enrolled_ids(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = response.parse()
            assert_matches_type(IndividualEnrolledIDsResponse, individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_many_benefits(self, client: Finch) -> None:
        individual = client.hris.benefits.individuals.retrieve_many_benefits(
            "string",
        )
        assert_matches_type(SyncSinglePage[IndividualBenefit], individual, path=["response"])

    @parametrize
    def test_method_retrieve_many_benefits_with_all_params(self, client: Finch) -> None:
        individual = client.hris.benefits.individuals.retrieve_many_benefits(
            "string",
            individual_ids="d675d2b7-6d7b-41a8-b2d3-001eb3fb88f6,d02a6346-1f08-4312-a064-49ff3cafaa7a",
        )
        assert_matches_type(SyncSinglePage[IndividualBenefit], individual, path=["response"])

    @parametrize
    def test_raw_response_retrieve_many_benefits(self, client: Finch) -> None:
        response = client.hris.benefits.individuals.with_raw_response.retrieve_many_benefits(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(SyncSinglePage[IndividualBenefit], individual, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_many_benefits(self, client: Finch) -> None:
        with client.hris.benefits.individuals.with_streaming_response.retrieve_many_benefits(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = response.parse()
            assert_matches_type(SyncSinglePage[IndividualBenefit], individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unenroll_many(self, client: Finch) -> None:
        individual = client.hris.benefits.individuals.unenroll_many(
            "string",
        )
        assert_matches_type(SyncSinglePage[UnenrolledIndividual], individual, path=["response"])

    @parametrize
    def test_method_unenroll_many_with_all_params(self, client: Finch) -> None:
        individual = client.hris.benefits.individuals.unenroll_many(
            "string",
            individual_ids=["string", "string", "string"],
        )
        assert_matches_type(SyncSinglePage[UnenrolledIndividual], individual, path=["response"])

    @parametrize
    def test_raw_response_unenroll_many(self, client: Finch) -> None:
        response = client.hris.benefits.individuals.with_raw_response.unenroll_many(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(SyncSinglePage[UnenrolledIndividual], individual, path=["response"])

    @parametrize
    def test_streaming_response_unenroll_many(self, client: Finch) -> None:
        with client.hris.benefits.individuals.with_streaming_response.unenroll_many(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = response.parse()
            assert_matches_type(SyncSinglePage[UnenrolledIndividual], individual, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndividuals:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_enroll_many(self, client: AsyncFinch) -> None:
        individual = await client.hris.benefits.individuals.enroll_many(
            "string",
            individuals=[{}],
        )
        assert_matches_type(AsyncSinglePage[EnrolledIndividual], individual, path=["response"])

    @parametrize
    async def test_raw_response_enroll_many(self, client: AsyncFinch) -> None:
        response = await client.hris.benefits.individuals.with_raw_response.enroll_many(
            "string",
            individuals=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(AsyncSinglePage[EnrolledIndividual], individual, path=["response"])

    @parametrize
    async def test_streaming_response_enroll_many(self, client: AsyncFinch) -> None:
        async with client.hris.benefits.individuals.with_streaming_response.enroll_many(
            "string",
            individuals=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(AsyncSinglePage[EnrolledIndividual], individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_enrolled_ids(self, client: AsyncFinch) -> None:
        individual = await client.hris.benefits.individuals.enrolled_ids(
            "string",
        )
        assert_matches_type(IndividualEnrolledIDsResponse, individual, path=["response"])

    @parametrize
    async def test_raw_response_enrolled_ids(self, client: AsyncFinch) -> None:
        response = await client.hris.benefits.individuals.with_raw_response.enrolled_ids(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(IndividualEnrolledIDsResponse, individual, path=["response"])

    @parametrize
    async def test_streaming_response_enrolled_ids(self, client: AsyncFinch) -> None:
        async with client.hris.benefits.individuals.with_streaming_response.enrolled_ids(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(IndividualEnrolledIDsResponse, individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_many_benefits(self, client: AsyncFinch) -> None:
        individual = await client.hris.benefits.individuals.retrieve_many_benefits(
            "string",
        )
        assert_matches_type(AsyncSinglePage[IndividualBenefit], individual, path=["response"])

    @parametrize
    async def test_method_retrieve_many_benefits_with_all_params(self, client: AsyncFinch) -> None:
        individual = await client.hris.benefits.individuals.retrieve_many_benefits(
            "string",
            individual_ids="d675d2b7-6d7b-41a8-b2d3-001eb3fb88f6,d02a6346-1f08-4312-a064-49ff3cafaa7a",
        )
        assert_matches_type(AsyncSinglePage[IndividualBenefit], individual, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_many_benefits(self, client: AsyncFinch) -> None:
        response = await client.hris.benefits.individuals.with_raw_response.retrieve_many_benefits(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(AsyncSinglePage[IndividualBenefit], individual, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_many_benefits(self, client: AsyncFinch) -> None:
        async with client.hris.benefits.individuals.with_streaming_response.retrieve_many_benefits(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(AsyncSinglePage[IndividualBenefit], individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unenroll_many(self, client: AsyncFinch) -> None:
        individual = await client.hris.benefits.individuals.unenroll_many(
            "string",
        )
        assert_matches_type(AsyncSinglePage[UnenrolledIndividual], individual, path=["response"])

    @parametrize
    async def test_method_unenroll_many_with_all_params(self, client: AsyncFinch) -> None:
        individual = await client.hris.benefits.individuals.unenroll_many(
            "string",
            individual_ids=["string", "string", "string"],
        )
        assert_matches_type(AsyncSinglePage[UnenrolledIndividual], individual, path=["response"])

    @parametrize
    async def test_raw_response_unenroll_many(self, client: AsyncFinch) -> None:
        response = await client.hris.benefits.individuals.with_raw_response.unenroll_many(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(AsyncSinglePage[UnenrolledIndividual], individual, path=["response"])

    @parametrize
    async def test_streaming_response_unenroll_many(self, client: AsyncFinch) -> None:
        async with client.hris.benefits.individuals.with_streaming_response.unenroll_many(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(AsyncSinglePage[UnenrolledIndividual], individual, path=["response"])

        assert cast(Any, response.is_closed) is True
