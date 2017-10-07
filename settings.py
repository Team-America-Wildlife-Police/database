# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:21:03 2017

@author: Joaquin
"""

DOMAIN =\
    { "post":
        { "schema": 
            { # scraped fields
            , "date_accessed": {"type":"datetime"}
            , "date_listed": {"type":"datetime"}
            , "description": {}
            , "keyword_tags": {}
            , "post_geolocation": { "type": "string" }
            , "reported_animal" : {"type": "string"}
            , "reported_how": {}
            , "reported_where": {}
            , "source": {"type":"string",
                         "allowed": 
                             [ "Ebay"
                              , "Gumtree"
                              , "Twitter"
                              ]
                        }
            
            , "price": {}
            , "quantity": {}
            , "species": {}
            , "title": { "type": "string" }
            , "unit": {} #kg, individuals, etc.
            , "url": {}
            , "username": {}
            , "uuid": {}
              # user - entered fields
            , "additional_notes": {}
            , "case_handler_contact_info": {}
            , "class": {}
            , "common_names": {}
            , "exporter_country": {}
            , "family": {}
            , "genus": {}
            , "importer_country": {}
            , "listing_type": 
                [ "Import request"
                , "Export offer"
                , "Commision"
                ]
            , "order": {} #taxonomy order
            , "purpose": {} #Trophy, medicine, taxidermy
            , "relevant_authorities": {}
            , "taxon": {}
            , "trader": {} #person
            , "verified by": {} #e.g. sergio.
            }
        }
    }