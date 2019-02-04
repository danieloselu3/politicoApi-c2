"""app/test/test_v1_party_create.py """

from tests.base_test import BaseTest
import json
class TestParties(BaseTest):
        """ Test endpoints  app/v1/parties """
        party1 =  {
                'name' : 'Party A',
                'hqAddress' : '22 jumpstreet',
                'logoUrl' : 'www.url.com/party.png',
                }
        party1b =  {
                'name' : 'Party B',
                'hqAddress' : '23 jumpstreet',
                'logoUrl' : 'www.url.com/party.png',
                }
        party2  = {
                'name' : 'Par',
                'hqAddress' : '21 jumpstreet',
                'logoUrl' : 'www.url.com/party.png',
        }
        party3  = {
                'name' : 'Par',
                'logoUrl' : 'www.url.com/party.png',
        }
        def test_create_party(self):
                """ api/v1/parties Post test """
                result = self.client().post('/api/v1/parties', data=self.party1 )
                dataCheck = json.loads(result.data)
                self.assertEqual(result.status_code, 201)
                self.assertTrue('status' in dataCheck)
                self.assertEqual(dataCheck['status'], 201)
                self. assertTrue('data' in dataCheck)
                self.assertTrue('id' in dataCheck['data'])
                self.assertTrue(isinstance(dataCheck['data']['id'], int ))
                self.assertEqual(dataCheck['data']['name'], self.party1['name'])
        
        def test_create_party_with_wrong_data(self):
                """ api/v1/parties Post test with invalid data"""
                result = self.client().post('/api/v1/parties', data=self.party2 )
                dataCheck = json.loads(result.data)
                result2 = self.client().post('/api/v1/parties', data=self.party3 )
                dataCheck2 = json.loads(result.data)

                self.assertEqual(result.status_code, 400)
                self.assertTrue('status' in dataCheck)
                self.assertEqual(dataCheck['status'], 400)
                self.assertTrue('error' in dataCheck)

                self.assertEqual(result2.status_code, 400)
                self.assertTrue('status' in dataCheck2)
                self.assertEqual(dataCheck2['status'], 400)
                self.assertTrue('error' in dataCheck2)


        def test_get_specifi_party_details(self):
                """tests for endpoint /api/v1/parties/<partyId>"""
                result1 =self.client().post('/api/v1/parties', data=self.party1 )
                result12 =self.client().post('/api/v1/parties', data=self.party1b )
                dataCheck = json.loads(result1.data)
                dataCheck2 = json.loads(result12.data)

                resultGet1 = self.client().get("/api/v1/parties/{}".format(dataCheck['data']['id']))
                resultGet2 = self.client().get("/api/v1/parties/{}".format(dataCheck2['data']['id']))
                self.assertEqual(resultGet1.status_code, 200)
                self.assertEqual(resultGet2.status_code, 200)

                dataCheckGet = json.loads(resultGet1.data)
                self.assertTrue('status' in dataCheckGet)
                self.assertTrue('data' in dataCheckGet)

                self.assertEqual(dataCheckGet['data']['name'], self.party1['name'])

