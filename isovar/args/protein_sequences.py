# Copyright (c) 2016. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function, division, absolute_import

from ..default_parameters import PROTEIN_SEQUENCE_LENGTH, MAX_PROTEIN_SEQUENCES_PER_VARIANT
from ..protein_sequences import (
    protein_sequences_generator_to_dataframe,
    reads_generator_to_protein_sequences_generator
)

from .rna_reads import allele_reads_generator_from_args

def add_protein_sequence_args(parser):
    """
    Extends an ArgumentParser instance with the following args:
        --protein-sequence-length
        --max-protein-sequences-per-variant
    """
    protein_sequence_group = parser.add_argument_group("Protein Sequence")
    protein_sequence_group.add_argument(
        "--protein-sequence-length",
        default=PROTEIN_SEQUENCE_LENGTH,
        type=int)
    protein_sequence_group.add_argument(
        "--max-protein-sequences-per-variant",
        type=int,
        default=MAX_PROTEIN_SEQUENCES_PER_VARIANT)
    return parser

def protein_sequences_generator_from_args(args):
    allele_reads_generator = allele_reads_generator_from_args(args)
    return reads_generator_to_protein_sequences_generator(
        allele_reads_generator,
        protein_sequence_length=args.protein_sequence_length,
        min_reads_supporting_cdna_sequence=args.min_reads_supporting_variant_sequence,
        min_transcript_prefix_length=args.min_transcript_prefix_length,
        max_transcript_mismatches=args.max_reference_transcript_mismatches,
        max_protein_sequences_per_variant=args.max_protein_sequences_per_variant)

def protein_sequences_dataframe_from_args(args):
    protein_sequences_generator = protein_sequences_generator_from_args(args)
    return protein_sequences_generator_to_dataframe(protein_sequences_generator)
