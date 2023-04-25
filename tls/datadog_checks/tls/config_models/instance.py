# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Literal, Optional, Sequence

from pydantic import BaseModel, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class MetricPatterns(BaseModel):
    class Config:
        allow_mutation = False

    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    allowed_versions: Optional[Sequence[str]]
    days_critical: Optional[float]
    days_warning: Optional[float]
    disable_generic_tags: Optional[bool]
    empty_default_hostname: Optional[bool]
    fetch_intermediate_certs: Optional[bool]
    intermediate_cert_refresh_interval: Optional[float]
    local_cert_path: Optional[str]
    metric_patterns: Optional[MetricPatterns]
    min_collection_interval: Optional[float]
    name: Optional[str]
    port: Optional[int]
    seconds_critical: Optional[int]
    seconds_warning: Optional[int]
    send_cert_duration: Optional[bool]
    server: str
    server_hostname: Optional[str]
    service: Optional[str]
    start_tls: Optional[Literal['postgres', 'mysql']]
    tags: Optional[Sequence[str]]
    timeout: Optional[int]
    tls_ca_cert: Optional[str]
    tls_cert: Optional[str]
    tls_private_key: Optional[str]
    tls_private_key_password: Optional[str]
    tls_validate_hostname: Optional[bool]
    tls_verify: Optional[bool]
    transport: Optional[str]

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))