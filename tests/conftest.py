"""
测试配置文件

定义共享的 fixtures 用于数据契约校验测试
"""

import pytest
import yaml
import csv
import pandas as pd
from pathlib import Path
from typing import Dict, List


# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
FIXTURES_ROOT = PROJECT_ROOT / "tests" / "fixtures"


@pytest.fixture
def fixtures_root():
    """返回 fixtures 根目录路径"""
    return FIXTURES_ROOT


@pytest.fixture
def workspace_root():
    """返回 workspace 目录路径"""
    return FIXTURES_ROOT / "workspace"


@pytest.fixture
def catelog_root(workspace_root):
    """返回 catelog 目录路径"""
    return workspace_root / "catelog"


@pytest.fixture
def public_root():
    """返回 public 目录路径"""
    return FIXTURES_ROOT / "public"


@pytest.fixture
def contract_root(catelog_root):
    """返回契约目录路径"""
    return catelog_root / "contract"


@pytest.fixture
def record_root(catelog_root):
    """返回记录目录路径"""
    return catelog_root / "record"


@pytest.fixture
def source_contract_path(contract_root):
    """返回原始数据契约文件路径"""
    return contract_root / "source-contract.yaml"


@pytest.fixture
def output_contract_path(contract_root):
    """返回输出数据契约文件路径"""
    return contract_root / "output-contract.yaml"


@pytest.fixture
def dirty_csv_path(record_root):
    """返回脏数据 CSV 文件路径"""
    return record_root / "dirty.csv"


@pytest.fixture
def clean_csv_path(record_root):
    """返回清洗后数据 CSV 文件路径"""
    return record_root / "clean.csv"


@pytest.fixture
def catalog_manifest_path(catelog_root):
    """返回数据目录清单文件路径"""
    return catelog_root / "catalog-manifest.yaml"


@pytest.fixture
def spec_root(public_root):
    """返回规格说明目录路径"""
    return public_root / "spec"


@pytest.fixture
def base_spec_path(spec_root):
    """返回基础规格说明文件路径"""
    return spec_root / "base_spec.md"


@pytest.fixture
def cleaning_spec_path(spec_root):
    """返回清洗规格说明文件路径"""
    return spec_root / "questionnaire_cleanning_spec.md"


@pytest.fixture
def base_spec(base_spec_path):
    """加载基础规格说明"""
    with open(base_spec_path, 'r', encoding='utf-8') as f:
        return f.read()


@pytest.fixture
def cleaning_spec(cleaning_spec_path):
    """加载清洗规格说明"""
    with open(cleaning_spec_path, 'r', encoding='utf-8') as f:
        return f.read()


@pytest.fixture
def source_contract(source_contract_path):
    """加载原始数据契约"""
    with open(source_contract_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture
def output_contract(output_contract_path):
    """加载输出数据契约"""
    with open(output_contract_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture
def dirty_data(dirty_csv_path):
    """加载脏数据"""
    with open(dirty_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.fixture
def clean_data(clean_csv_path):
    """加载清洗后数据"""
    with open(clean_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.fixture
def dirty_df(dirty_csv_path):
    """加载脏数据为 DataFrame"""
    return pd.read_csv(dirty_csv_path)


@pytest.fixture
def clean_df(clean_csv_path):
    """加载清洗后数据为 DataFrame"""
    return pd.read_csv(clean_csv_path)


@pytest.fixture
def catalog_manifest(catalog_manifest_path):
    """加载数据目录清单"""
    with open(catalog_manifest_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture
def source_columns(source_contract):
    """提取原始数据契约中的列定义"""
    if 'dataset' not in source_contract or not source_contract['dataset']:
        return []
    return source_contract['dataset'][0].get('columns', [])


@pytest.fixture
def output_columns(output_contract):
    """提取输出数据契约中的列定义"""
    if 'dataset' not in output_contract or not output_contract['dataset']:
        return []
    return output_contract['dataset'][0].get('columns', [])


@pytest.fixture
def expected_record_count():
    """预期的记录数量"""
    return {
        'dirty': 19,
        'clean': 19,
        'unique': 18  # dirty 去重后
    }


@pytest.fixture
def quality_flags():
    """数据质量标签定义"""
    return {
        'normal': '正常',
        'income_missing': '收入缺失',
        'key_fields_missing': '关键字段缺失',
        'student_logic': '逻辑校验_学生',
        'retiree_logic': '逻辑校验_退休',
        'duplicate': '重复记录',
        'test_data': '测试数据',
        'anomaly_negative_income': '异常值_收入负数_工作负荷越界'
    }


@pytest.fixture
def type_mapping():
    """字段类型映射"""
    return {
        'id': 'integer',
        'submit_time': 'datetime',
        'age': 'integer',
        'total_exp': 'integer',
        'dept': 'string',
        'overall_satis': 'integer',
        'workload': 'integer',
        'benefit_pension': 'boolean',
        'benefit_annual_leave': 'boolean',
        'benefit_health_ins': 'boolean',
        'benefit_other': 'boolean',
        'other_notes': 'string',
        'gender': 'string',
        'edu': 'string',
        'emp_status': 'string',
        'tenure': 'float',
        'monthly_income': 'float',
        'city': 'string',
        'is_duplicate': 'boolean',
        'data_quality_flag': 'string'
    }


@pytest.fixture
def constraints():
    """字段约束定义"""
    return {
        'age': {'min': 16, 'max': 120, 'not_null': False},
        'total_exp': {'min': 0, 'not_null': False},
        'overall_satis': {'min': 1, 'max': 5, 'not_null': False},
        'workload': {'min': 1, 'max': 5, 'not_null': False},
        'tenure': {'min': 0, 'not_null': False},
        'monthly_income': {'not_null': False},
        'id': {'not_null': True}
    }
