# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:21:03 2017

@author: Joaquin
"""

DOMAIN =\
    { "post":
        { "schema": 
            { # scraped fields
             "date_listed": {"type":"datetime"}
            , "date_accessed": {"type":"datetime"}
            , "post_geolocation": { "type": "string" }
            , "reported_animal" : {"type": "string"}
            , "reported_how": {}
            , "reported_where": {}
            , "source": [ "Ebay"
                        , "Gumtree"
                        , "Twitter"
                        ]
            
            , "description": {}
            , "keyword tags": []
            , "price": {}
            , "quantity": {}
            , "species": {}
            , "title": { "type": "string" }
            , "unit": {} #kg, individuals, etc.
            , "url": {}
            , "username": {}
            
              # user - entered fields
            , "additional_notes": {}
            , "class": {}
            , "common_names": {}
            , "case_handler_contact_info": {}
            , "exporter_country": {}
            , "family": {}
            , "genus": {}
            , "importer_country": {}
            , "listing_type": 
                [ "Import request"
                , "Export offer"
                , "Commision"
                ]
            , "order": {}
            , "purpose": {} #Trophy, medicine, taxidermy
            , "relevant_authorities": {}
            , "taxon": {}
            , "trader": {} #person
            , "verified by": {} #e.g. sergio.
            }
        }
    }