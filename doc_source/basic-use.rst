.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

###############
Using the |TVS|
###############

.. meta::
    :description: Basic use of the AWS Toolkit for Visual Studio.
    :keywords: profile, service

    .. topic:: Adding a profile to the SDK Credential Store

Profiles and |TVS| Window Binding
=================================

The AWS Explorer window is bound to a single profile and region at a time. 

* Windows opened from the AWS Explorer use the current bound profile and region. Once 
  the window is open, you can switch to another profile or region in the AWS Explorer.

* Publish and other wizards default to the profile and region of the AWS Explorer. You
  can change them. Any resources created by the wizard, or windows opened when
  the wizard closes, will continue to use the profile and region selected in the
  wizard.

* If you have multiple Visual Studio open, each can be bound to a different profile
  and region. The AWS Explorer saves the last-used profile and region. The last
  Visual Studio instanced closed will have its values persisted.

