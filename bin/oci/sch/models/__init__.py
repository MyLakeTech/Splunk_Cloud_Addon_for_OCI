# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_service_connector_compartment_details import ChangeServiceConnectorCompartmentDetails
from .create_service_connector_details import CreateServiceConnectorDetails
from .dimension_details import DimensionDetails
from .dimension_value_details import DimensionValueDetails
from .function_task_details import FunctionTaskDetails
from .functions_target_details import FunctionsTargetDetails
from .jmes_path_dimension_value import JmesPathDimensionValue
from .latest_streaming_cursor import LatestStreamingCursor
from .log_rule_task_details import LogRuleTaskDetails
from .log_source import LogSource
from .logging_analytics_target_details import LoggingAnalyticsTargetDetails
from .logging_source_details import LoggingSourceDetails
from .monitoring_source import MonitoringSource
from .monitoring_source_all_metrics import MonitoringSourceAllMetrics
from .monitoring_source_details import MonitoringSourceDetails
from .monitoring_source_metric_details import MonitoringSourceMetricDetails
from .monitoring_source_namespace_details import MonitoringSourceNamespaceDetails
from .monitoring_source_selected_namespace import MonitoringSourceSelectedNamespace
from .monitoring_source_selected_namespace_details import MonitoringSourceSelectedNamespaceDetails
from .monitoring_target_details import MonitoringTargetDetails
from .notifications_target_details import NotificationsTargetDetails
from .object_storage_target_details import ObjectStorageTargetDetails
from .service_connector import ServiceConnector
from .service_connector_collection import ServiceConnectorCollection
from .service_connector_summary import ServiceConnectorSummary
from .source_details import SourceDetails
from .static_dimension_value import StaticDimensionValue
from .streaming_cursor_details import StreamingCursorDetails
from .streaming_source_details import StreamingSourceDetails
from .streaming_target_details import StreamingTargetDetails
from .target_details import TargetDetails
from .task_details import TaskDetails
from .trim_horizon_streaming_cursor import TrimHorizonStreamingCursor
from .update_service_connector_details import UpdateServiceConnectorDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for sch services.
sch_type_mapping = {
    "ChangeServiceConnectorCompartmentDetails": ChangeServiceConnectorCompartmentDetails,
    "CreateServiceConnectorDetails": CreateServiceConnectorDetails,
    "DimensionDetails": DimensionDetails,
    "DimensionValueDetails": DimensionValueDetails,
    "FunctionTaskDetails": FunctionTaskDetails,
    "FunctionsTargetDetails": FunctionsTargetDetails,
    "JmesPathDimensionValue": JmesPathDimensionValue,
    "LatestStreamingCursor": LatestStreamingCursor,
    "LogRuleTaskDetails": LogRuleTaskDetails,
    "LogSource": LogSource,
    "LoggingAnalyticsTargetDetails": LoggingAnalyticsTargetDetails,
    "LoggingSourceDetails": LoggingSourceDetails,
    "MonitoringSource": MonitoringSource,
    "MonitoringSourceAllMetrics": MonitoringSourceAllMetrics,
    "MonitoringSourceDetails": MonitoringSourceDetails,
    "MonitoringSourceMetricDetails": MonitoringSourceMetricDetails,
    "MonitoringSourceNamespaceDetails": MonitoringSourceNamespaceDetails,
    "MonitoringSourceSelectedNamespace": MonitoringSourceSelectedNamespace,
    "MonitoringSourceSelectedNamespaceDetails": MonitoringSourceSelectedNamespaceDetails,
    "MonitoringTargetDetails": MonitoringTargetDetails,
    "NotificationsTargetDetails": NotificationsTargetDetails,
    "ObjectStorageTargetDetails": ObjectStorageTargetDetails,
    "ServiceConnector": ServiceConnector,
    "ServiceConnectorCollection": ServiceConnectorCollection,
    "ServiceConnectorSummary": ServiceConnectorSummary,
    "SourceDetails": SourceDetails,
    "StaticDimensionValue": StaticDimensionValue,
    "StreamingCursorDetails": StreamingCursorDetails,
    "StreamingSourceDetails": StreamingSourceDetails,
    "StreamingTargetDetails": StreamingTargetDetails,
    "TargetDetails": TargetDetails,
    "TaskDetails": TaskDetails,
    "TrimHorizonStreamingCursor": TrimHorizonStreamingCursor,
    "UpdateServiceConnectorDetails": UpdateServiceConnectorDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}