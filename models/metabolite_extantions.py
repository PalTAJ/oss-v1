'''Extantion Methods for Metabolites'''

import math
import json

import cobra as cb
from .model_extantions import *


def connected_subsystems(self):
    '''Connected Subsystem of metabolite'''
    return set([r.subsystem for r in self.reactions])


def is_border(self):
    ''' Extantion method to check metabolite in model is border'''
    return len(self.connected_subsystems()) > 1


def is_currency(self, by='subsystem'):
    ''' Extantion method to check metabolite in model is currency'''
    if self.id in self.currency_list:
        return True
    if by == 'reaction':
        return len(self.reactions) >= self.currency_threshold
    elif by == 'subsystem':
        return len(self.connected_subsystems()) > self.currency_threshold
    else:
        raise ValueError('by should be either subsystem or reactions')


def producers(self, without_transports=False):
    reactions = filter(lambda r: r.metabolites[self] > 0, self.reactions)
    if without_transports:
        reactions = filter(
            lambda r: not cb.Model.is_transport_subsystem(r.subsystem),
            reactions)
    return list(reactions)


def consumers(self):
    return [r for r in self.reactions if r.metabolites[self] < 0]


def total_stoichiometry(self, without_transports=False):
    return sum(r.metabolites[self] for r in self.producers(without_transports))


cb.Metabolite.connected_subsystems = connected_subsystems
cb.Metabolite.is_border = is_border
cb.Metabolite.currency_threshold = math.inf
cb.Metabolite.currency_list = set(
    json.load(open('../dataset/currency/currency_metabolites.json')))
cb.Metabolite.is_currency = is_currency
cb.Metabolite.producers = producers
cb.Metabolite.consumers = consumers
cb.Metabolite.total_stoichiometry = total_stoichiometry
